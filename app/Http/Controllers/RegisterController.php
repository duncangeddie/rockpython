<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RegisterController extends Controller
{
    public function index()
    {
        // Variables for the register view
        $RegisterPage = [
            'background' => 'register_background.png',
            'logo'       => 'logo_short.png',
            'heading'    => 'Create Your Account',
            'subtext'    => 'Join us and get started',
        ];

        return view('auth.register', compact('RegisterPage'));
    }
}
