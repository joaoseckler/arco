<?php
    echo "<p>";

    if(file_exists('file.mid')) {
        unlink('file.mid'); //remove the file
    }
    if (move_uploaded_file($_FILES['userfile']['tmp_name'], 'file.mid')) {
        echo "Deu certo, clique no botão abaixo para baixar o arquivo:\n";
    } else {
        echo "Not uploaded because of error #".$_FILES["file"]["error"];
    }
    echo "</p>";

    shell_exec("./midi.py");
    echo '<a style="border: 2px solid black" href="file.ino">file.ino</a>';
?>

<br>
<br>
<a href="instrument.ino">Ou clique aqui para acessar o código que torna o arduino num instrumento MIDI</a>
