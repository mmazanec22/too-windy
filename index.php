<html>
<head>
  <title>Is it too windy to bike today?</title>
</head>
<body>
  <div>
    <?php
    // run python script, get data from file into one string
    exec('python3 get_local_wind_speed.py 60640');
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
    ?>
  </div>
  <!-- default home page: -->
    <!-- Want to know if it will be too windy to bike?  Enter your zip code. -->
    <!-- [zip code entry box] -->
  <!-- home page with params: -->
    <!-- YES or NO -->
    <!-- The highest predicted wind speed between now and midnight for your zip code is  -->
    <!-- bookmark this page! -->
  <footer>Powered by <a href="https://darksky.net/poweredby/">Dark Sky</a>.</footer>
</body>
</html>