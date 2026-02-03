<x-app-layout>
    <style>
        body {
            background: url('{{ asset('dashboard_images/' . ($DashboardPage['background'] ?? 'dashboard_background.png')) }}') no-repeat center center fixed;
            background-size: cover;
        }
    </style>

    <!-- Optional: add content here -->

</x-app-layout>
