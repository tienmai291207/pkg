# -*- coding: utf-8 -*-
import telebot
import psutil
import platform

# Thay bằng mã token của bạn
API_TOKEN = '7162238846:AAEDv4luhK0Txn43DYLBTn6DoVOUntbvBxM'

# Khởi tạo bot
bot = telebot.TeleBot(API_TOKEN)

# Xử lý lệnh /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn đến với bot! Sử dụng lệnh /cpu để kiểm tra cấu hình máy.")

# Xử lý lệnh /cpu
@bot.message_handler(commands=['cpu'])
def handle_cpu(message):
    # Lấy thông tin hệ thống
    uname_info = platform.uname()
    cpu_info = platform.processor()
    memory_info = psutil.virtual_memory()
    
    # Tạo thông báo
    cpu_message = (
        f"Thông tin cấu hình máy:\n"
        f"System: {uname_info.system}\n"
        f"Node Name: {uname_info.node}\n"
        f"Release: {uname_info.release}\n"
        f"Version: {uname_info.version}\n"
        f"Machine: {uname_info.machine}\n"
        f"Processor: {cpu_info}\n"
        f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n"
        f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB\n"
        f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB\n"
        f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB\n"
    )
    
    # Gửi thông tin đến người dùng
    bot.reply_to(message, cpu_message)

# Chạy bot
bot.polling()
