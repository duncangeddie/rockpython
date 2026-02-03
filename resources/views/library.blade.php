<x-app-layout>
    <style>
        body {
            background: url('{{ asset('library_images/' . $LibraryPage['background']) }}') no-repeat center center fixed;
            background-size: cover;
        }
    </style>

    <div class="library-topics">
        <!-- Topic 1 -->
        <a href="{{ $LibraryPage['topic1_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic1_icon']) }}" alt="{{ $LibraryPage['topic1_label'] }} Icon">
            <span>{{ $LibraryPage['topic1_label'] }}</span>
        </a>

        <!-- Topic 2 -->
        <a href="{{ $LibraryPage['topic2_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic2_icon']) }}" alt="{{ $LibraryPage['topic2_label'] }} Icon">
            <span>{{ $LibraryPage['topic2_label'] }}</span>
        </a>

        <!-- Topic 3 -->
        <a href="{{ $LibraryPage['topic3_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic3_icon']) }}" alt="{{ $LibraryPage['topic3_label'] }} Icon">
            <span>{{ $LibraryPage['topic3_label'] }}</span>
        </a>

        <!-- Topic 4 -->
        <a href="{{ $LibraryPage['topic4_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic4_icon']) }}" alt="{{ $LibraryPage['topic4_label'] }} Icon">
            <span>{{ $LibraryPage['topic4_label'] }}</span>
        </a>

        <!-- Topic 5 -->
        <a href="{{ $LibraryPage['topic5_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic5_icon']) }}" alt="{{ $LibraryPage['topic5_label'] }} Icon">
            <span>{{ $LibraryPage['topic5_label'] }}</span>
        </a>

        <!-- Topic 6 -->
        <a href="{{ $LibraryPage['topic6_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic6_icon']) }}" alt="{{ $LibraryPage['topic6_label'] }} Icon">
            <span>{{ $LibraryPage['topic6_label'] }}</span>
        </a>

        <!-- Topic 7 -->
        <a href="{{ $LibraryPage['topic7_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic7_icon']) }}" alt="{{ $LibraryPage['topic7_label'] }} Icon">
            <span>{{ $LibraryPage['topic7_label'] }}</span>
        </a>

        <!-- Topic 8 -->
        <a href="{{ $LibraryPage['topic8_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic8_icon']) }}" alt="{{ $LibraryPage['topic8_label'] }} Icon">
            <span>{{ $LibraryPage['topic8_label'] }}</span>
        </a>

        <!-- Topic 9 -->
        <a href="{{ $LibraryPage['topic9_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic9_icon']) }}" alt="{{ $LibraryPage['topic9_label'] }} Icon">
            <span>{{ $LibraryPage['topic9_label'] }}</span>
        </a>

        <!-- Topic 10 -->
        <a href="{{ $LibraryPage['topic10_link'] }}" class="library-topic">
            <img src="{{ asset($LibraryPage['topic10_icon']) }}" alt="{{ $LibraryPage['topic10_label'] }} Icon">
            <span>{{ $LibraryPage['topic10_label'] }}</span>
        </a>
    </div>
</x-app-layout>
