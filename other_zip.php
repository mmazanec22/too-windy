<html>
<head>
  <title>Is it too windy to bike today?</title>
  <link rel="stylesheet" type="text/css" href="style.php"/>
</head>
<body>
  <div class = "all-contents">
    <?php
      // run python script, get data from file into one string
      if(strlen((int)$_GET["user-zip"]) == 5 && is_numeric($_GET["user-zip"])) {
        exec('python3 get_local_wind_speed.py ' . $_GET["user-zip"]);
        $filename = "last_call_file.txt";
        $handle = fopen($filename, "r");
        $contents = fread($handle, filesize($filename));
        fclose($handle);
        // parse string into an array and assign variables
        $file_contents_array = explode("\n", $contents);
        $currentSpeed = $file_contents_array[0];
        $strongestWindString = $file_contents_array[1];
        $alerts = $file_contents_array[2];

        if($currentSpeed > 15.0){
          echo "<h1> Yes. </h1>";
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

    <form action="other_zip.php" method="get">
      <label>Check another zip code: </label>
      <input type="text" name="user-zip">
      <input type="submit">
    </form>

    <br>
    <br>

    <footer>Created by <a href="https://github.com/mmazanec22/too-windy">Melanie Mazanec</a>.  Powered by <a target="_blank" href="https://darksky.net/poweredby/">Dark Sky</a>.</footer>
  </div>
</body>
</html>