<html>
<head>
  <title>Is it too windy to bike today?</title>
  <link rel="stylesheet" type="text/css" href="style.php"/>
</head>
<body>
  <div class = "all-contents">
    <?php

      // run python script
      exec('python3 get_local_wind_speed.py 60640');

      // get data from file into one string
      $filename = "60640.txt";
      $handle = fopen($filename, "r");
      $contents = fread($handle, filesize($filename));
      fclose($handle);

      // parse string into an array and assign variables
      $file_contents_array = explode("\n", $contents);
      $currentSpeed = $file_contents_array[0];
      $strongestWindString = $file_contents_array[1];

      if($currentSpeed > 15.0){
        echo "<h1> Yes. </h1>";
      }
      else if($currentSpeed == "!"){
        echo "<h1> ! </h1>"; // this is what the script passes for too many API
      }
      else {
        echo "<h1> No. </h1>";
      }
      echo "<h2>" . $strongestWindString . "</h2>";
    ?>

    <form oninput="x.value=parseInt(mph.value)" action="other_zip.php" method="get">
      <br>
      <label>Check another zip code: </label>
      <input type="text" name="user-zip">
      <div class= "set-mph">
        <br>
        <label>How windy is too windy?</label>
        <output name="x" for="mph" value = "15">15</output> mph
        <input type="range" name="mph" min="10" max="30" value="15">
      </div>
      <div>
        <br>
        <input type="submit" value = "Check Zip" class = "submit-button">
      </div>
    </form>

    <br>
    <br>

    <footer>Created by <a href="https://github.com/mmazanec22/too-windy">Melanie Mazanec</a>.  Powered by <a target="_blank" href="https://darksky.net/poweredby/">Dark Sky</a>.</footer>
    <?php
      exec('python3 zip_code_file_cleanup.py');
    ?>
  </div>
</body>
</html>