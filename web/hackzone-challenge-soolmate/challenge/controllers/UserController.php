<?php
class UserController
{
    public function index($router)
    {
        $input = isset($_GET['name']) ? $_GET['name'] : 'Eliot Alderson';
        $user = new UserModel($input);
        return $router->view('index', ['user' => $user->getUser()]);
    }
}