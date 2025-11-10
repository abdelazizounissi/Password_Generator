# 🔐 Password Generator

A modern, user-friendly password generator application with a sleek GUI built using Python and Tkinter. Generate strong, customizable passwords with just a few clicks!

## ✨ Features

- **Customizable Length**: Set password length according to your needs
- **Multiple Character Types**: Choose from:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Clean Modern UI**: Dark-themed interface for comfortable viewing
- **User-Friendly**: Simple and intuitive design

## 📋 Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## 🚀 Installation & Usage

### Option 1: Run from Source

1. Clone this repository:
```bash
git clone https://github.com/abdelazizounissi/Password_Generator.git
cd Password_Generator
```

2. Run the application:
```bash
python password.py
```

**Note**: Make sure `lock.ico` is in the same directory as `password.py` for the icon to display properly.

### Option 2: Download Pre-Built Application

Download the ready-to-use application:
- **[PasswordGenerator_App.zip](PasswordGenerator_App.zip)** - Standalone executable application (no Python installation required)

Simply download, extract, and run the application!

## 🎯 How to Use

1. **Set Password Length**: Enter your desired password length (default is 12)
2. **Select Character Types**: Check the boxes for the types of characters you want to include:
   - Uppercase (A-Z)
   - Lowercase (a-z)
   - Digits (0-9)
   - Symbols (!@#$%)
3. **Generate**: Click the "Generate" button to create your password
4. **Copy**: Click the "Copy" button to copy the password to your clipboard

⚠️ **Note**: You must select at least one character type to generate a password.

## 🖼️ Screenshots

<img width="493" height="467" alt="image" src="https://github.com/user-attachments/assets/bf22fe74-7b00-4c41-b923-1ee3f34e2040" />



## 🔒 Security Note

This password generator uses Python's `random` module which is suitable for most purposes. For cryptographically secure random number generation, consider using `secrets` module for highly sensitive applications.

## 🛠️ Building Executable (Optional)

If you want to create your own standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=lock.ico password.py
```

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**Abdelaziz Ounissi**

© 2025 Abdelaziz Ounissi

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

**Enjoy creating strong, secure passwords! 🔐**
