<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\RegisterController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\LibraryController;

Route::get('/', function () {
    if (auth()->check()) {
        return redirect()->route('dashboard');
    }
    return (new WelcomeController)->index();
});

Route::get('/login', [LoginController::class, 'index'])->name('login');
Route::get('/register', [RegisterController::class, 'index'])->name('register');

Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::get('/library', [LibraryController::class, 'index'])->name('library');

    Route::get('/library/topic1', [LibraryController::class, 'topic1'])->name('library.topic1');
    Route::get('/library/topic2', [LibraryController::class, 'topic2'])->name('library.topic2');
    Route::get('/library/topic3', [LibraryController::class, 'topic3'])->name('library.topic3');
    Route::get('/library/topic4', [LibraryController::class, 'topic4'])->name('library.topic4');
    Route::get('/library/topic5', [LibraryController::class, 'topic5'])->name('library.topic5');
    Route::get('/library/topic6', [LibraryController::class, 'topic6'])->name('library.topic6');
    Route::get('/library/topic7', [LibraryController::class, 'topic7'])->name('library.topic7');
    Route::get('/library/topic8', [LibraryController::class, 'topic8'])->name('library.topic8');
    Route::get('/library/topic9', [LibraryController::class, 'topic9'])->name('library.topic9');
    Route::get('/library/topic10', [LibraryController::class, 'topic10'])->name('library.topic10');
});
