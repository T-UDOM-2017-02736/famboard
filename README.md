# 🏠 FamBoard: Your Family Dashboard

Welcome to **FamBoard**, a web-based household dashboard designed to streamline your family's chores, meals, events, and more. This project aims to simplify household management, making it easier for families to stay organized and connected.

[![Download Latest Release](https://img.shields.io/badge/Download%20Latest%20Release-v1.0.0-blue)](https://github.com/T-UDOM-2017-02736/famboard/releases)

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Features

FamBoard offers a range of features to help families manage their daily tasks efficiently:

- **Chores Management**: Assign and track household chores for each family member.
- **Meal Planning**: Organize meals for the week, including grocery lists.
- **Event Scheduling**: Keep track of family events and appointments.
- **User-Friendly Interface**: Easy to navigate, designed for all ages.
- **Mobile-Friendly**: Access FamBoard on any device, including smartphones and tablets.
- **Offline Capabilities**: Works even without an internet connection, thanks to PWA support.
- **Raspberry Pi Support**: Run your dashboard on a Raspberry Pi for a home server experience.

## Technologies Used

FamBoard is built using the following technologies:

- **Flask**: A lightweight Python web framework.
- **SQLite**: A simple, lightweight database for storing data.
- **Python**: The primary programming language used for backend development.
- **HTML/CSS/JavaScript**: For frontend development.
- **Progressive Web App (PWA)**: Enhances the user experience by allowing offline access.
- **Raspberry Pi**: For those who want to host their own instance.

## Installation

To get started with FamBoard, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/T-UDOM-2017-02736/famboard.git
   cd famboard
   ```

2. **Install Dependencies**:

   Make sure you have Python and pip installed. Then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:

   Initialize the SQLite database:

   ```bash
   python setup_db.py
   ```

4. **Run the Application**:

   Start the Flask server:

   ```bash
   python app.py
   ```

5. **Access the Dashboard**:

   Open your web browser and go to `http://127.0.0.1:5000`.

For the latest release, [download it here](https://github.com/T-UDOM-2017-02736/famboard/releases) and follow the same installation steps.

## Usage

Once you have the application running, you can begin using FamBoard:

1. **Create an Account**: Sign up to create your family profile.
2. **Add Family Members**: Invite family members to join the dashboard.
3. **Manage Chores**: Assign chores to family members and track their progress.
4. **Plan Meals**: Use the meal planner to organize weekly meals.
5. **Schedule Events**: Add events to the calendar and set reminders.

The user interface is designed to be intuitive. You can navigate through different sections easily, making household management a breeze.

## Contributing

We welcome contributions to FamBoard! If you want to help improve the project, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button on the top right corner.
2. **Create a New Branch**:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Make Your Changes**: Implement your feature or fix a bug.
4. **Commit Your Changes**:

   ```bash
   git commit -m "Add Your Feature"
   ```

5. **Push to Your Branch**:

   ```bash
   git push origin feature/YourFeature
   ```

6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request."

We appreciate your help in making FamBoard better!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out:

- **Email**: support@famboard.com
- **GitHub Issues**: Use the Issues tab in this repository for bug reports or feature requests.

---

Thank you for checking out FamBoard! We hope it helps you and your family stay organized and connected. For the latest updates, be sure to check the [Releases](https://github.com/T-UDOM-2017-02736/famboard/releases) section.