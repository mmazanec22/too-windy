<html>
<head>
  <title>Is it too windy to bike today?</title>
  <link rel="stylesheet" type="text/css" href="style.php"/>
</head>
<body>
  <div class = "all-contents">
    <?php

      // check to see if zip code is valid
      if(strlen((int)$_GET["user-zip"]) == 5 && is_numeric($_GET["user-zip"])) {


        // run python script with input zip
        exec('python3 get_local_wind_speed.py ' . $_GET["user-zip"]);

        // SAME AS INDEX FROM HERE...
        $filename = "last_call_file.txt";
        $handle = fopen($filename, "r");
        $contents = fread($handle, filesize($filename));
        fclose($handle);

        // parse string into an array and assign variables
        $file_contents_array = explode("\n", $contents);
        $currentSpeed = $file_contents_array[0];
        $strongestWindString = $file_contents_array[1];
        $alerts = $file_contents_array[2];
        // TO HERE

        if($currentSpeed > $_GET["mph"]){
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
        <input type="submit" value = "Check Zip">
      </div>
    </form>

    <br>
    <br>

    <footer>Created by <a href="https://github.com/mmazanec22/too-windy">Melanie Mazanec</a>.  Powered by <a target="_blank" href="https://darksky.net/poweredby/">Dark Sky</a>.</footer>
  </div>
</body>
</html>