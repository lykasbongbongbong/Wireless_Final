# CovidHelper: Body Temperature Measurement and Automatic Notification System

This is a sw-hw integration IoT application delivered by Raspberry Pi, LoRa and Python. 
As COVID-19 pandemic burst out, students have to be taken body temperature at each entering fo school building, which is really a cumbersome work as schools have to allocate extra personnel at each entrance, might perhaps have those personnel exposed under even greater risk get infected. 
Therefore, our team integrated IoT devices and software system and created a fully-automatic system for body temperature measurement and alert report notification. 

這個軟硬體整合系統提供疫情下在學校場館各個入口的體溫量測與警示服務。從體溫量測、判斷體溫是否正常至寄送量測報告，達成全自動化服務，減少人事成本與感染風險。

---
## System Workflow


 

## How to use?
學生量測體溫並記錄對應學號<br>
 case 0: 體溫<30度 => 重新量測，不寄信。<br>
 case 1: 30<體溫<37.5 => 正常，出席，寄信給學生(Student is healthy!)<br>
 case 2: 體溫>=37.5 => 不正常，不能出席，寄信給學生(Student is burning!)><br>
 
在預設班級大小(10位)同學都量測完體溫後，寄信給老師得到上課資料。

要成功執行寄信的功能：
```
cd send_ttn.py
```
修改這部分：
```
zUser = '寄件人地址'
zPass = '信箱密碼'
zTo = '收件人地址'
```

資料庫安裝 MariaDB
1. 安裝之前先確認到最新的版本
```
# apt update
# apt upgrade
```
2. 安裝MariaDB-server
```
# apt install mariadb-server
# mysql_secure_installation
# mysql -u root -p
```
3. 建立資料庫
```
sudo mysql
CREATE DATABASE class;
```
3. 建立資料表
```
CREATE TABLE students(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
attendance TINYINT(2) NOT NULL
) 
```
> attendance會以三種數值表示出缺席： 0(尚未量測體溫) / 1(已量測體溫並出席) / -1(已量測體溫但無法出席)


