<x-app-layout>
    <head>
        <link rel="stylesheet" href="{{ asset('css/librarytopic3.css') }}">
    </head>

    <style>
        body {
            background: url('{{ asset('library_images/' . $TopicPage['background']) }}') no-repeat center center fixed;
            background-size: cover;
        }
    </style>
</x-app-layout>
