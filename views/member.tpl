<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="bootstrap.min.css">
	<title>Ekki leynisíða</title>
    <style>
        body{
            margin: 3em;
        }

        h2{
            color: #a00
            font-family: sans-serif;
        }
    </style>
</head>
<body>
    <h2>Félagskrá</h2>
    <p>Te member team are as follows:</p>

    <table class="table table-striped">
    %for row in rows:
        <tr>
        %for col in row:
            <td>{{col}}</td>
        %end
        </tr>
    %end
    </table>
</body>
</html>
