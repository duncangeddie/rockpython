<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LibraryController extends Controller
{
    public function index()
    {
        $LibraryPage = [
            'background' => 'library_background.png',

            'topic1_label' => 'Abstract Classes',
            'topic1_icon' => 'library_images/library_topic1_icon.png',
            'topic1_link' => '/library/topic1',

            'topic2_label' => 'Algorithms',
            'topic2_icon' => 'library_images/library_topic2_icon.png',
            'topic2_link' => '/library/topic2',

            'topic3_label' => 'Asyncio',
            'topic3_icon' => 'library_images/library_topic3_icon.png',
            'topic3_link' => '/library/topic3',

            'topic4_label' => 'Attributes',
            'topic4_icon' => 'library_images/library_topic4_icon.png',
            'topic4_link' => '/library/topic4',

            'topic5_label' => 'Bitwise Operators',
            'topic5_icon' => 'library_images/library_topic5_icon.png',
            'topic5_link' => '/library/topic5',

            'topic6_label' => 'Boolean Logic',
            'topic6_icon' => 'library_images/library_topic6_icon.png',
            'topic6_link' => '/library/topic6',

            'topic7_label' => 'Classes',
            'topic7_icon' => 'library_images/library_topic7_icon.png',
            'topic7_link' => '/library/topic7',

            'topic8_label' => 'Comprehensions',
            'topic8_icon' => 'library_images/library_topic8_icon.png',
            'topic8_link' => '/library/topic8',

            'topic9_label' => 'Concurrency',
            'topic9_icon' => 'library_images/library_topic9_icon.png',
            'topic9_link' => '/library/topic9',

            'topic10_label' => 'Context Managers',
            'topic10_icon' => 'library_images/library_topic10_icon.png',
            'topic10_link' => '/library/topic10',
        ];

        return view('library', compact('LibraryPage'));
    }

    public function topic1()
    {
        $TopicPage = [
            'background' => 'library_topic1_background.png',
            'label' => 'Abstract Classes',
            'icon' => 'library_images/library_topic1_icon.png',
        ];

        return view('library-topic1', compact('TopicPage'));
    }

    public function topic2()
    {
        $TopicPage = [
            'background' => 'library_topic2_background.png',
            'label' => 'Algorithms',
            'icon' => 'library_images/library_topic2_icon.png',
        ];

        return view('library-topic2', compact('TopicPage'));
    }

    public function topic3()
    {
        $TopicPage = [
            'background' => 'library_topic3_background.png',
            'label' => 'Asyncio',
            'icon' => 'library_images/library_topic3_icon.png',
        ];

        return view('library-topic3', compact('TopicPage'));
    }

    public function topic4()
    {
        $TopicPage = [
            'background' => 'library_topic4_background.png',
            'label' => 'Attributes',
            'icon' => 'library_images/library_topic4_icon.png',
        ];

        return view('library-topic4', compact('TopicPage'));
    }

    public function topic5()
    {
        $TopicPage = [
            'background' => 'library_topic5_background.png',
            'label' => 'Bitwise Operators',
            'icon' => 'library_images/library_topic5_icon.png',
        ];

        return view('library-topic5', compact('TopicPage'));
    }

    public function topic6()
    {
        $TopicPage = [
            'background' => 'library_topic6_background.png',
            'label' => 'Boolean Logic',
            'icon' => 'library_images/library_topic6_icon.png',
        ];

        return view('library-topic6', compact('TopicPage'));
    }

    public function topic7()
    {
        $TopicPage = [
            'background' => 'library_topic7_background.png',
            'label' => 'Classes',
            'icon' => 'library_images/library_topic7_icon.png',
        ];

        return view('library-topic7', compact('TopicPage'));
    }

    public function topic8()
    {
        $TopicPage = [
            'background' => 'library_topic8_background.png',
            'label' => 'Comprehensions',
            'icon' => 'library_images/library_topic8_icon.png',
        ];

        return view('library-topic8', compact('TopicPage'));
    }

    public function topic9()
    {
        $TopicPage = [
            'background' => 'library_topic9_background.png',
            'label' => 'Concurrency',
            'icon' => 'library_images/library_topic9_icon.png',
        ];

        return view('library-topic9', compact('TopicPage'));
    }

    public function topic10()
    {
        $TopicPage = [
            'background' => 'library_topic10_background.png',
            'label' => 'Context Managers',
            'icon' => 'library_images/library_topic10_icon.png',
        ];

        return view('library-topic10', compact('TopicPage'));
    }
}
