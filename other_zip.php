<html>
<head>
  <title>Is it too windy to bike today?</title>
  <link rel="stylesheet" type="text/css" href="style.php"/>
</head>
<body>
  <div class = "all-contents">
    <?php
      // check to see if zip code is valid
      $inputZip = str_replace(" ", "", $_GET["user-zip"]);
      if(strlen($inputZip) == 5 && is_numeric($inputZip)) {

        // run python script with input zip
        exec('python3 scripts/get_local_wind_speed.py ' . $inputZip);

        $filename = $inputZip . ".txt";
        if(is_file($filename)){
          $handle = fopen($filename, "r");
          $contents = fread($handle, filesize($filename));
          fclose($handle);
          $file_contents_array = explode("\n", $contents);
          $currentSpeed = (double)$file_contents_array[0];
          $strongestWindString = $file_contents_array[1];
        }
        else{
          $currentSpeed = "!";
          $strongestWindString = "Do you even zip code, bro?";
        }

        // parse string into an array and assign variables

        if($currentSpeed > (double)$_GET["mph"]){
          echo "<h1> Yes. </h1>";
        }
        else if($currentSpeed == "!"){
          echo "<h1> ! </h1>";
        }
        else {
          echo "<h1> No. </h1>";
        }
        echo "<h2>" . $strongestWindString . "</h2>";
      }
      else{
        echo "<h1> Do you even zip code, bro? </h1>";
      }
    ?>

    <form oninput="x.value=parseInt(mph.value)" action="other_zip.php" method="get">
      <br>
      <label>Check another zip code: </label>
      <input type="text" name="user-zip">
      <div class= "set-mph">
        <br>
        <label>How windy is too windy?</label>
        <output name="x" for="mph" value = "15"><?php echo $_GET["mph"] ?></output> mph
        <?php echo '<input type="range" name="mph" min="10" max="30" value="' . $_GET["mph"] . '">' ?>
      </div>
      <div>
        <br>
        <input type="submit" value = "Check Zip" class = "submit-button">
      </div>
    </form>

    <div class="footer">
      <?php include 'partials/footer.php'; ?>
    </div>

  </div>
</body>
</html>