<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class WelcomeController extends Controller
{
    public function index()
    {
        return view('welcome', [
            'PageHeader' => 'Welcome to RockPython 🚀',
            'WelcomeParagraph' => [
                'RockPython is a site dedicated to covering all aspects of Python.',
                'Sign in or create an account to explore the Python language.'
            ],
            'WelcomeCards' => [
                [
                    'heading' => 'Python Code Base',
                    'text' => 'Explore a rich collection of Python code snippets and libraries.'
                ],
                [
                    'heading' => 'Starter Projects',
                    'text' => 'Kickstart your learning with beginner-friendly Python projects.'
                ],
                [
                    'heading' => 'Blog',
                    'text' => 'Read articles and tutorials on Python best practices.'
                ],
            ],
        ]);
    }
}
