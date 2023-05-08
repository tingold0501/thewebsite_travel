<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $phone = $_POST['phone'];
  $number = $_POST['number'];
  $date = $_POST['date'];
  $time = $_POST['time'];
  $message = $_POST['message'];

  // Gửi email tới địa chỉ email của admin
  $to = 'huynhtin0501@gmail.com';
  $subject = 'New Contact Form Submission';
  $messageBody = "Name: $name\nEmail: $email\nPhone: $phone\nNumber: $number\nDate: $date\nTime: $time\nMessage: $message";
  $headers = "From: $email";

  if (mail($to, $subject, $messageBody, $headers)) {
    echo "OK"; // Gửi phản hồi thành công về phía client-side
  } else {
    echo "Failed to send email"; // Gửi phản hồi thất bại về phía client-side
  }
}
?>
