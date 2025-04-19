import os
import unittest
import tempfile
from otpgen import OTPGen, KEYSTORE_FILE

class TestOTPGen(unittest.TestCase):
    def setUp(self):
        self.app = OTPGen()
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_secret = "JBSWY3DPEHPK3PXP"  # Base32 for "Hello!"

        # Simulate a keystore with valid entries
        self.password = b"testpass123"
        self.entries = [
            f"1 {self.test_secret} totp otpgen-test test@example.com",
            f"2 {self.test_secret} hotp otpgen-hot hot@example.com 0"
        ]
        self.app.get_password = lambda: self.password
        self.app.password = self.password  # <-- SET THIS
        self.app.store = self.entries.copy()
        self.app.encrypt_store()

    def tearDown(self):
        if os.path.exists(KEYSTORE_FILE):
            os.remove(KEYSTORE_FILE)
        os.unlink(self.temp_file.name)

    def test_decrypt_valid_password(self):
        self.app.get_password = lambda: self.password
        self.app.decrypt_store()
        self.assertEqual(len(self.app.store), 2)

    def test_decrypt_invalid_password(self):
        self.app.password = b"wrongpass"  # Force wrong password
        result = self.app.decrypt_store()
        self.assertFalse(result)

    def test_generate_totp_token(self):
        self.app.get_password = lambda: self.password
        token = self.app.generate_token("1", no_clip=True)
        self.assertTrue(token.isdigit() and len(token) >= 6)

    def test_generate_hotp_token(self):
        self.app.get_password = lambda: self.password
        token = self.app.generate_token("2", no_clip=True)
        self.assertTrue(token.isdigit())

    def test_list_keys_output(self):
        self.app.get_password = lambda: self.password
        self.app.decrypt_store()
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        self.app.list_keys()
        sys.stdout = sys.__stdout__
        self.assertIn("otpgen-test", captured.getvalue())

    def test_remove_key(self):
        self.app.get_password = lambda: self.password
        self.app.remove_key("1")
        self.app.decrypt_store()
        ids = [line.split()[0] for line in self.app.store]
        self.assertNotIn("1", ids)

    def test_export_import_json(self):
        path = self.temp_file.name + ".json"
        self.app.get_password = lambda: self.password
        self.app.export_keys("json", path=path)

        self.app.remove_key("1")
        self.app.remove_key("2")
        self.app.import_keys(path, fmt="json")
        self.app.decrypt_store()
        self.assertEqual(len(self.app.store), 2)

    def test_export_import_csv(self):
        path = self.temp_file.name + ".csv"
        self.app.get_password = lambda: self.password
        self.app.export_keys("csv", path=path)

        self.app.remove_key("1")
        self.app.remove_key("2")
        self.app.import_keys(path, fmt="csv")
        self.app.decrypt_store()
        self.assertEqual(len(self.app.store), 2)

    def test_generate_qr(self):
        self.app.get_password = lambda: self.password
        out_file = self.temp_file.name + ".png"
        self.app.generate_qr("1", out_file=out_file)
        self.assertTrue(os.path.exists(out_file))

    def test_generate_qr_missing_id(self):
        self.app.get_password = lambda: self.password
        with self.assertLogs(level="ERROR") as cm:
            self.app.generate_qr("9999")
            self.assertIn("Key not found", "".join(cm.output))

if __name__ == "__main__":
    unittest.main()
