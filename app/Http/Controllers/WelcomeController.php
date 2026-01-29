<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class WelcomeController extends Controller
{
    public function index()
    {
        return view('welcome', [
            'IntroBlock' => [
                'image'   => 'welcome_banner.png', // store in public/welcome_images/
                'heading' => 'Welcome to RockPython',
                'text'    => 'Your hub for Python projects, code snippets, and tutorials.',
            ],
            'WelcomeCards' => [
                [
                    'heading' => 'Python Code Base',
                    'text'    => 'Explore a rich collection of Python code snippets and libraries.',
                ],
                [
                    'heading' => 'DIY Projects',
                    'text'    => 'Kickstart your learning with beginner-friendly and advanced Python projects.',
                ],
                [
                    'heading' => 'Blog',
                    'text'    => 'Regular updates on Python',
                ],
                [
                    'heading' => 'Contact Us',
                    'text'    => 'Feel free to contact me if you would like a specific tutorial or project',
                ],
            ],
        ]);
    }
}
