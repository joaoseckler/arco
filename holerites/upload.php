<?php
    $upload_folder="files";
    echo "<p>";
    if (move_uploaded_file($_FILES['userfile']['tmp_name'], $upload_folder . '/in.pdf')) {
        echo "Deu certo, aqui estão os holerites:.\n";
    } else {
        echo "Alguma coisa deu errado...";
        exit(1);
    }

    shell_exec("./generate.sh");

    echo "<ul>";
    $dir = new DirectoryIterator($upload_folder);
    foreach ($dir as $fileinfo) {
        if (!$fileinfo->isDot()) {
            echo "<li><a href=\"" . $fileinfo->getFilename() . "\">" . $fileinfo->getFilename() . "</a></li>";
        }
    }
    echo "</ul>";
?>
