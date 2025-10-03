# Flask User Management System

A modern web application built with Flask that allows you to manage user profiles with full CRUD (Create, Read, Update, Delete) operations. Users can be added through a form, viewed in a list, and have individual profile pages with options to view or delete their information.

## 🚀 Features

- **User Registration**: Add new users with name, email, city, and hobby information
- **User Listing**: View all users in a clean, responsive table format
- **User Profiles**: Individual profile pages for each user
- **User Management**: Delete users from the system
- **Responsive Design**: Built with Bootstrap for mobile-friendly interface
- **Database Integration**: MySQL database for persistent data storage
- **Navigation**: Easy navigation between different sections

## 🛠️ Tech Stack

- **Backend**: Python 3.x with Flask
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Database Connector**: mysql-connector-python

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- MySQL Server
- pip (Python package installer)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd flask-user-management
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv sysenv

# Activate virtual environment
# On Windows:
sysenv\Scripts\activate
# On macOS/Linux:
source sysenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

1. **Start MySQL Server** and create a new database:

```sql
CREATE DATABASE user_management;
```

2. **Create the users table**:

```sql
USE user_management;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    hobby VARCHAR(50) NOT NULL
);
```

3. **Configure Database Connection**:

Edit `app.py` and update the database connection settings:

```python
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="your_username",        # Replace with your MySQL username
    password="your_password",    # Replace with your MySQL password
    database="user_management"
)
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📖 Usage & Examples

### Home Page (`/`)
- Welcome page with navigation options
- Quick access to "Add User" and "View Users" features

### Add User (`/add`)
- **GET**: Displays the user registration form
- **POST**: Processes form submission and adds user to database

**Form Fields:**
- Name (required)
- Email (required, email validation)
- City (required)
- Hobby (required)

### View Users (`/users`)
- Displays all users in a responsive table
- Shows: Name, Email, City, Hobby
- Action buttons: "View Profile" and "Delete"

### User Profile (`/user/<id>`)
- Individual profile page for each user
- Displays complete user information
- Navigation back to user list

### Delete User (`/delete/<id>`)
- Removes user from database
- Redirects back to user list after deletion

## 🗄️ Database Schema

### Users Table

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `id` | INT, PK, Auto Increment | Unique user identifier |
| `user_name` | VARCHAR(50) | Full name of the user |
| `email` | VARCHAR(100) | Email address |
| `city` | VARCHAR(50) | City name |
| `hobby` | VARCHAR(50) | User's hobby |

## 🎨 Project Structure

```
flask-user-management/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── sysenv/               # Virtual environment
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── home.html         # Home page
    ├── add_user.html     # Add user form
    ├── users.html        # User listing page
    └── profile.html      # Individual user profile
```

## 🚀 Getting Started

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Add your first user**:
   - Click "Add User" button
   - Fill in the form with user details
   - Submit to add to database

4. **View users**:
   - Click "View Users" to see all registered users
   - Click "View Profile" to see individual user details
   - Click "Delete" to remove users

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and test thoroughly
4. **Commit your changes**:
   ```bash
   git commit -m "Add: Description of your changes"
   ```
5. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Add comments for complex logic
- Test your changes before submitting
- Update documentation if needed

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify MySQL server is running
   - Check username/password in `app.py`
   - Ensure database `user_management` exists

2. **Port Already in Use**:
   - Change port in `app.py`: `app.run(port=5001, debug=True)`

3. **Module Not Found**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed description

---

**Happy Coding! 🎉**
