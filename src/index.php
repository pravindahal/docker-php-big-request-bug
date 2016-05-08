<?php

$expectedContentLength = $_SERVER["CONTENT_LENGTH"] ?? 0;

$realContentLength = strlen(file_get_contents('php://input'));

header('Content-type', 'application/json');

echo json_encode([
    'success'               => ($realContentLength == $expectedContentLength),
    'expectedContentLength' => $expectedContentLength,
    'realContentLength'     => $realContentLength,
]);
