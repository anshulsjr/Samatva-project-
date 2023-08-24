<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];
    $profession = $_POST["profession"];
    $membershipType = $_POST["membership-type"];
    
    // Handle uploaded file
    if (isset($_FILES["photo"])) {
        $photoName = $_FILES["photo"]["name"];
        $photoTmpName = $_FILES["photo"]["tmp_name"];
        $photoPath = "uploads/" . $photoName; // Change the path as needed
        move_uploaded_file($photoTmpName, $photoPath);
    }
    
    // Now you can save the data to a database or perform other actions
    // For demonstration purposes, we'll just print the data
    echo "Name: $name<br>";
    echo "Email: $email<br>";
    echo "Phone: $phone<br>";
    echo "Profession: $profession<br>";
    echo "Membership Type: $membershipType<br>";
    
    if (isset($photoName)) {
        echo "Profile Photo: <img src='$photoPath' alt='Profile Photo'><br>";
    }
}
?>
