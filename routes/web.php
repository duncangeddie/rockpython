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

    Route::get('/library/topic11', [LibraryController::class, 'topic11'])->name('library.topic11');
    Route::get('/library/topic12', [LibraryController::class, 'topic12'])->name('library.topic12');
    Route::get('/library/topic13', [LibraryController::class, 'topic13'])->name('library.topic13');
    Route::get('/library/topic14', [LibraryController::class, 'topic14'])->name('library.topic14');
    Route::get('/library/topic15', [LibraryController::class, 'topic15'])->name('library.topic15');
    Route::get('/library/topic16', [LibraryController::class, 'topic16'])->name('library.topic16');
    Route::get('/library/topic17', [LibraryController::class, 'topic17'])->name('library.topic17');
    Route::get('/library/topic18', [LibraryController::class, 'topic18'])->name('library.topic18');
    Route::get('/library/topic19', [LibraryController::class, 'topic19'])->name('library.topic19');
    Route::get('/library/topic20', [LibraryController::class, 'topic20'])->name('library.topic20');

    Route::get('/library/topic21', [LibraryController::class, 'topic21'])->name('library.topic21');
    Route::get('/library/topic22', [LibraryController::class, 'topic22'])->name('library.topic22');
    Route::get('/library/topic23', [LibraryController::class, 'topic23'])->name('library.topic23');
    Route::get('/library/topic24', [LibraryController::class, 'topic24'])->name('library.topic24');
    Route::get('/library/topic25', [LibraryController::class, 'topic25'])->name('library.topic25');
    Route::get('/library/topic26', [LibraryController::class, 'topic26'])->name('library.topic26');
    Route::get('/library/topic27', [LibraryController::class, 'topic27'])->name('library.topic27');
    Route::get('/library/topic28', [LibraryController::class, 'topic28'])->name('library.topic28');
    Route::get('/library/topic29', [LibraryController::class, 'topic29'])->name('library.topic29');
    Route::get('/library/topic30', [LibraryController::class, 'topic30'])->name('library.topic30');

    Route::get('/library/topic31', [LibraryController::class, 'topic31'])->name('library.topic31');
    Route::get('/library/topic32', [LibraryController::class, 'topic32'])->name('library.topic32');
    Route::get('/library/topic33', [LibraryController::class, 'topic33'])->name('library.topic33');
    Route::get('/library/topic34', [LibraryController::class, 'topic34'])->name('library.topic34');
    Route::get('/library/topic35', [LibraryController::class, 'topic35'])->name('library.topic35');
    Route::get('/library/topic36', [LibraryController::class, 'topic36'])->name('library.topic36');
    Route::get('/library/topic37', [LibraryController::class, 'topic37'])->name('library.topic37');
    Route::get('/library/topic38', [LibraryController::class, 'topic38'])->name('library.topic38');
    Route::get('/library/topic39', [LibraryController::class, 'topic39'])->name('library.topic39');
    Route::get('/library/topic40', [LibraryController::class, 'topic40'])->name('library.topic40');

    Route::get('/library/topic41', [LibraryController::class, 'topic41'])->name('library.topic41');
    Route::get('/library/topic42', [LibraryController::class, 'topic42'])->name('library.topic42');
    Route::get('/library/topic43', [LibraryController::class, 'topic43'])->name('library.topic43');
    Route::get('/library/topic44', [LibraryController::class, 'topic44'])->name('library.topic44');
    Route::get('/library/topic45', [LibraryController::class, 'topic45'])->name('library.topic45');
    Route::get('/library/topic46', [LibraryController::class, 'topic46'])->name('library.topic46');
    Route::get('/library/topic47', [LibraryController::class, 'topic47'])->name('library.topic47');
    Route::get('/library/topic48', [LibraryController::class, 'topic48'])->name('library.topic48');
    Route::get('/library/topic49', [LibraryController::class, 'topic49'])->name('library.topic49');
    Route::get('/library/topic50', [LibraryController::class, 'topic50'])->name('library.topic50');

    Route::get('/library/topic51', [LibraryController::class, 'topic51'])->name('library.topic51');
    Route::get('/library/topic52', [LibraryController::class, 'topic52'])->name('library.topic52');
    Route::get('/library/topic53', [LibraryController::class, 'topic53'])->name('library.topic53');
    Route::get('/library/topic54', [LibraryController::class, 'topic54'])->name('library.topic54');
    Route::get('/library/topic55', [LibraryController::class, 'topic55'])->name('library.topic55');
    Route::get('/library/topic56', [LibraryController::class, 'topic56'])->name('library.topic56');
    Route::get('/library/topic57', [LibraryController::class, 'topic57'])->name('library.topic57');
    Route::get('/library/topic58', [LibraryController::class, 'topic58'])->name('library.topic58');
    Route::get('/library/topic59', [LibraryController::class, 'topic59'])->name('library.topic59');
    Route::get('/library/topic60', [LibraryController::class, 'topic60'])->name('library.topic60');

    Route::get('/library/topic61', [LibraryController::class, 'topic61'])->name('library.topic61');
    Route::get('/library/topic62', [LibraryController::class, 'topic62'])->name('library.topic62');
    Route::get('/library/topic63', [LibraryController::class, 'topic63'])->name('library.topic63');
    Route::get('/library/topic64', [LibraryController::class, 'topic64'])->name('library.topic64');
    Route::get('/library/topic65', [LibraryController::class, 'topic65'])->name('library.topic65');
    Route::get('/library/topic66', [LibraryController::class, 'topic66'])->name('library.topic66');
    Route::get('/library/topic67', [LibraryController::class, 'topic67'])->name('library.topic67');
    Route::get('/library/topic68', [LibraryController::class, 'topic68'])->name('library.topic68');
    Route::get('/library/topic69', [LibraryController::class, 'topic69'])->name('library.topic69');
    Route::get('/library/topic70', [LibraryController::class, 'topic70'])->name('library.topic70');
    Route::get('/library/topic71', [LibraryController::class, 'topic71'])->name('library.topic71');
    Route::get('/library/topic72', [LibraryController::class, 'topic72'])->name('library.topic72');
    Route::get('/library/topic73', [LibraryController::class, 'topic73'])->name('library.topic73');
    Route::get('/library/topic74', [LibraryController::class, 'topic74'])->name('library.topic74');
});
