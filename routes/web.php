<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\RegisterController;
use App\Http\Controllers\DashboardController;

// Root route: redirect based on authentication
Route::get('/', function () {
    if (auth()->check()) {
        return redirect()->route('dashboard');
    }
    // Call the controller properly (not statically)
    return (new WelcomeController)->index();
});

// Auth routes
Route::get('/login', [LoginController::class, 'index'])->name('login');
Route::get('/register', [RegisterController::class, 'index'])->name('register');

// Protected routes (only for signed-in + verified users)
Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
});

