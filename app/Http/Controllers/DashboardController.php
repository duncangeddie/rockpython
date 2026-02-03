<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DashboardController extends Controller
{
    public function index()
    {
        $DashboardPage = [
            'logo' => 'logo_short.png',
            'background' => 'dashboard_background.png',
        ];

        return view('dashboard', compact('DashboardPage'));
    }
}
