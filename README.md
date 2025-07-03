# Odoo E-commerce Manager

![Odoo](https://img.shields.io/badge/Odoo-17-875A7B.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Overview

A comprehensive e-commerce management system built on Odoo 17, featuring intelligent workflow management, role-based security, and automated reporting.

## ✨ Features

- **Product Management**: Complete catalog with pricing and inventory
- **Order Workflow**: Intelligent state management (Draft → Confirmed → Delivered)
- **User Roles**: Granular permissions (Sales Staff / Manager)
- **Automated Reports**: PDF generation for orders
- **Real-time Messaging**: Built-in communication system

## 🛠️ Tech Stack

- **Backend**: Odoo 17 (Python)
- **Database**: PostgreSQL 15
- **Frontend**: Odoo Web Client
- **Architecture**: MVC Pattern

## 🚀 Quick Start

### Installation

1. **Clone the repository**

```bash
https://github.com/nahom-23/online_store_management.git
cd Odoo-Ecommerce-Manager
```

2. **Start the services**

3. **Access the application**

- URL: <http://localhost:8069>
- Username: `admin`
- Password: `admin`

4. **Install the module**

- Go to Apps → Update Apps List
- Search for "Management store"
- Click Install

## 📖 Usage

### Managing Products

1. Navigate to **Managment storen** → **Product**
2. Click **Create** to add new products
3. Set pricing and descriptions

### Processing Orders

1. Go to **Managment store** → **Orders**
2. Create new orders and add products
3. Use workflow buttons: Confirm → Deliver
4. Generate PDF reports with the Print button

### User Management

1. Access **Settings** → **Users & Companies**
2. Assign roles: Sales Staff or Manager
3. Configure permissions per role

## 🏗️ Architecture

```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │    │   Odoo Server   │    │   PostgreSQL    │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│   (Database)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                    ┌─────────────────┐
                    │  Custom Module  │
                    │ Odoo-Ecommerce-Manager │
                    └─────────────────┘

### Key Models

#### **Product Model (`management.product`)**

- Name, description, price fields
- Category management
- Inventory tracking

#### **Order Model (`management.order`)**

- Customer relationship
- Product selection (Many2many)
- Workflow states: Draft → Confirmed → Delivered
- Automatic total calculation
- PDF report generation

### Adding Features

1. Create models in `models/`
2. Define views in `views/`
3. Set permissions in `security/`
4. Update `__manifest__.py`

## 🔐 Security System

### User Roles

- **Sales Staff**: Can view products, manage orders
- **Manager**: Full administrative access

### Permissions Matrix

| Resource | Sales Staff | Manager |
|----------|-------------|---------|
| Products | Read | Full CRUD |
| Orders | Read/Create/Write | Full CRUD |
| Reports | Generate | Full Access |

## 📋 Business Logic

### Order Workflow

1. **Draft**: Initial state, editable
2. **Confirmed**: Order validated, ready for processing
3. **Delivered**: Order completed
4. **Cancelled**: Order cancelled

### Automatic Features

- **Sequential numbering** for orders
- **Real-time total calculation**
- **Mail thread integration** for communication
- **PDF report generation**



## 📸 Screenshots

| Feature | Description |
|---------|-------------|
| Dashboard | Main navigation and overview |
| Products | Product catalog management |
| Orders | Order processing workflow |
| Reports | PDF generation system |

---
⭐ **Star this repository if it helped you!**
