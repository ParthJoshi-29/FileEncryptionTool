# FIL-11: Testing & QA Report - FileEncryptionTool 🔐

## 🔧 Module: Encryption and Decryption (Tested by: Soham Bodh)

---

## ✅ Summary

Tested encryption/decryption workflows with various edge cases and handled errors as part of FIL-10. This file documents all test cases and results.

---

## 🧪 Test Cases

| TC ID | Test Description                   | Steps                               | Expected Result            | Actual Result                      | Status  |
| ----- | ---------------------------------- | ----------------------------------- | -------------------------- | ---------------------------------- | ------- |
| TC-01 | Encrypt valid file                 | Upload test.txt → Click Encrypt     | File saved as test.txt.enc | ✅ test.txt.enc generated          | ✅ Pass |
| TC-02 | Decrypt valid `.enc` file          | Upload test.txt.enc → Click Decrypt | File saved as test.txt     | ✅ File decrypted correctly        | ✅ Pass |
| TC-03 | Decrypt with wrong key             | Replaced `key.key` with invalid key | Show error message         | ✅ "Decryption failed" flash shown | ✅ Pass |
| TC-04 | No file uploaded                   | Click Encrypt with no file          | Show "No file uploaded!"   | ✅ Flash message displayed         | ✅ Pass |
| TC-05 | Decrypt non-encrypted file         | Upload regular file → Click Decrypt | Show decryption failed     | ✅ Flash shown                     | ✅ Pass |
| TC-06 | Key file missing                   | Delete `key.key` and try decrypt    | Flash: Key not found       | ✅ Correct flash message shown     | ✅ Pass |
| TC-07 | Encrypt special character filename | résumé.pdf → Click Encrypt          | File is saved properly     | ✅ résumé.pdf.enc created          | ✅ Pass |
| TC-08 | Encrypt large file                 | Upload 50MB file → Encrypt          | File encrypts successfully | ✅ No crash                        | ✅ Pass |
| TC-09 | Decrypt corrupt file               | Upload broken.enc file → Decrypt    | Show decryption failed     | ✅ Handled gracefully              | ✅ Pass |
| TC-10 | Unexpected file type               | Upload image.png → Encrypt          | File encrypted             | ✅ Successfully handled            | ✅ Pass |

---

## 🐞 Bugs Found

- N/A (All test cases passed)

---

## 🔄 Recommendations

- Add file type restriction (e.g., block `.exe`)
- Add progress bar for large files
- Auto-delete uploaded files after some time

---

## 👨‍💻 Tester

**Name:** Soham Bodh  
**Jira Issue:** FIL-11  
**Date:** April 17, 2025
