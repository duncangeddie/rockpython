<x-app-layout>
    <style>
        body {
            background: url('{{ asset('library_images/' . $TopicPage['background']) }}') no-repeat center center fixed;
            background-size: cover;
        }
    </style>

    <h1 class="page-header">{{ $TopicPage['label'] }}</h1>
</x-app-layout>

