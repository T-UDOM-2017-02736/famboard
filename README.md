# 🏠 Family Dashboard

A modular, web-based household dashboard built with Flask and SQLite. Designed to help manage chores, meal planning, events, savings goals, and more. Built to run locally on a Raspberry Pi or any home server.

---

## ✨ Features

### 💼 Chores System
- Per-user pages to track and complete daily tasks
- Admin dashboard to add, remove, and reassign chores
- Auto-calculates weekly earnings

### 📅 Events Calendar
- Add and view shared events, appointments, and reminders
- Optimized for mobile dashboard view

### 🍽 Meal Planning
- Input weekly dinner plans
- Future: AI suggestions and grocery integration

### 💰 Savings Goals
- Track progress toward individual savings goals
- Supports multiple users

---

## ⚙️ Tech Stack
- Python 3
- Flask
- SQLite3
- HTML/CSS (static front-end)

Runs fast on a Raspberry Pi (tested on Pi 4 with <500MB RAM usage).

---

## ⚡ Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/family-dashboard.git
cd family-dashboard
```

### 2. Initialize the database
```bash
python3 init_db.py
```

### 3. Run the Flask app
```bash
sudo python3 app.py
```
By default, the server runs on port 80 and is accessible on your local network.

---

## 📱 Pages
| Path | Description |
|------|-------------|
| `/user1` | Page for User 1 |
| `/user2` | Page for User 2 |
| `/parent` | Admin control panel |
| `/dashboard` | Unified view with chores, meals, and events |

---

## 🗂 Database Schema

**Tables:**
- `chores`
- `meals`
- `events`
- `goals`

Schema definitions are in `init_db.py`.

---

## 👨‍💼 Contributing
Pull requests and forks welcome! Ideal starter project for:
- Home automation tinkerers
- Families who like digital dashboards
- Raspberry Pi hobbyists

---

## 🕁️ Roadmap Ideas
- [ ] Turn into installable PWA
- [ ] Add AI-generated meal suggestions
- [ ] Push notifications
- [ ] Password-protected admin view

---

## 🔒 License
MIT License. Built for home use, modify freely!
