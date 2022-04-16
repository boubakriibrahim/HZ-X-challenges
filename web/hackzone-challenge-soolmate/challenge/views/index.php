<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>
<html>
<head>
  <meta name='author' content='makelaris, makelarisjr'>
  <meta charset="UTF-8">
  <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
  <title> Time To Finish </title>
  <link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'>
  <link rel='stylesheet' href='//cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css' integrity='sha512-HK5fgLBL+xu6dm/Ii3z4xhlSUyZgTT9tuc/hSrtw6uzJOvgRr2a9jyxxT1ely+B+xFAmJKVSTbpM/CuL7qxO8w==' crossorigin='anonymous' />

</head>
<body>
<div id='main' class='container'>
  <h1 id='title'>
    <i class='fas fa-heart pulse'></i> <b>SoolMeeting</b> <i class='fas fa-heart pulse'></i>
  </h1>
  <br>
  <h2>Your Soolmate :</h2> 
  <br>
  <span id='user'> <?= $user ?></span>
  <div class='form-group'>
    <a href='?name=Eliot Alderson' class='btn-lg btn-danger btn-block text-center'>See Eliot Soolmate</a>
  </div>
</div>
</body>
</html>