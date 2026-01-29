<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RockPython</title>

    <!-- Load Inter font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ asset('css/welcome.blade.css') }}">
</head>

<body>
    <!-- Header -->
    <header>
        <div class="logo">
            <img src="{{ asset('logo/logo_full.png') }}" alt="RockPython Logo">
        </div>

        <div class="auth-buttons">
            @if (Route::has('login'))
                <a href="{{ route('login') }}">Login</a>
            @endif

            @if (Route::has('register'))
                <a href="{{ route('register') }}">Register</a>
            @endif
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <h1>{{ $PageHeader }}</h1>

        <p class="welcome-text">
            @foreach ($WelcomeParagraph as $line)
                {{ $line }}<br>
            @endforeach
        </p>

        <div class="cards">
            @foreach ($WelcomeCards as $card)
                <div class="card">
                    <img src="{{ asset('placeholder/image_placeholder.png') }}" alt="{{ $card['heading'] }}">
                    <h2>{{ $card['heading'] }}</h2>
                    <p>{{ $card['text'] }}</p>
                </div>
            @endforeach
        </div>
    </main>
</body>
</html>
