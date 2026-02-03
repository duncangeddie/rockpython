<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LoginController extends Controller
{
    public function index()
    {
        // Variables for the login view
        $LoginPage = [
            'background' => 'login_background.png',
            'logo'       => 'logo_short.png',
            'heading'    => 'Welcome Back',
            'subtext'    => 'Please log in to continue',
        ];

        return view('auth.login', compact('LoginPage'));
    }
}
