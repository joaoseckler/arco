<?php
    $output = shell_exec("python3 create_labels.py 2>&1");
    echo '<p><a href="etiquetas.pdf">Etiquetas</a></p>';
    echo '<p><pre>';
    echo nl2br($output);
    echo '</pre></p>'
?>
