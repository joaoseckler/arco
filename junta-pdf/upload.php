<?php
    $upload_folder="files";
    echo "<p>";
    if (move_uploaded_file($_FILES['userfile1']['tmp_name'], $upload_folder . '/in1.pdf')) {
        echo "Deu certo, aqui estão os pdfs juntados:.\n";
    } else {
        echo "Alguma coisa deu errado...\n";
    }

    if (move_uploaded_file($_FILES['userfile2']['tmp_name'], $upload_folder . '/in2.zip')) {
        echo "Deu certo, aqui estão os pdfs juntados:.\n";
    } else {
        echo "Alguma coisa deu errado...\n";
    }

    shell_exec("./generate.sh");

    echo "<ul>";
    $dir = new DirectoryIterator($upload_folder);
    foreach ($dir as $fileinfo) {
        if (!$fileinfo->isDot()) {
            echo "<li><a href=\"files/" . $fileinfo->getFilename() . "\">" . $fileinfo->getFilename() . "</a></li>";
        }
    }
    echo "</ul>";
?>
