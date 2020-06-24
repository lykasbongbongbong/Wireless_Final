# wireless_final 

這是一個幫助老師了解學生出缺席狀況的小幫手！

流程：
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


