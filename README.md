# Odoo Helpdesk Kementerian Dalam Negeri

## Prerequisites
- Git 
- Python >= 3.6
- Pycharm 
- Database PostgreSQL >= 10

## Setup Awal

### 1. Buat folder kosong di komputer lokal
```
C:\Helpdesk
```
### 2. Buat 2 buah folder dalam folder tersebut
```
C:\Helpdesk\server
C:\Helpdesk\custom
```

### 3. Clone source code asli odoo ke dalam folder _server_
```
cd C:\Helpdesk\server
git clone https://github.com/OCA/OCB.git --depth 1 --branch 16.0 .
```
<sub>PENTING: perhatikan tanda TITIK di akhir baris ini, tidak boleh ketinggalan ini untuk meng-clone code ke dalam CURRENT FOLDER</sub>

### 4. Clone source code custom kita ke dalam folder _custom_
```
cd C:\Helpdesk\custom
git clone git@github.com:WannaBeStart/odoo16-mendagri.git
```

### 5. Buka Pycharm dan create new project, arahkan ke folder yang tadi sudah kita buat

### 6. Setup python Virtual Environment

### 7. Setup file odoo.conf

### 8. Install requirements 
```
cd C:\Helpdesk\server 
pip install -r requirements.txt
```

