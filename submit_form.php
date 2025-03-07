<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);

    // Validate form data (basic validation)
    if (empty($name) || empty($email) || empty($message)) {
        echo "All fields are required.";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit;
    }

    // Set the recipient email address
    $to = "business@pingpro.in"; 

    // Set the subject of the email
    $subject = "Message from $name via Contact Form";

    // Create the email body content
    $body = "Name: $name\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message";

    // Set email headers
    $headers = "From: $email" . "\r\n";
    $headers .= "Reply-To: $email" . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8" . "\r\n";

    // Send the email using PHP's mail() function
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for contacting us! We will get back to you shortly.";
    } else {
        echo "Message could not be sent. Please try again later.";
    }
}
?>
