<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DashboardController extends Controller
{
    public function index()
    {
        $DashboardPage = [
            'background' => 'dashboard_background.png',
            'logo' => 'logo_short.png',
        ];

        return view('dashboard', compact('DashboardPage'));
    }
}

