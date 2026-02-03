<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LibraryController extends Controller
{
    public function index()
    {
        $LibraryPage = [
            'background' => 'library_background.png',

            // Topic 1
            'topic1_label' => 'Abstract Classes',
            'topic1_icon' => 'library_images/library_icon_abstract.png',
            'topic1_link' => '#',

            // Topic 2
            'topic2_label' => 'Algorithms',
            'topic2_icon' => 'library_images/library_icon_algorithm.png',
            'topic2_link' => '#',

            // Topic 3
            'topic3_label' => 'Asyncio',
            'topic3_icon' => 'library_images/library_icon_asyncio.png',
            'topic3_link' => '#',

            // Topic 4
            'topic4_label' => 'Attributes',
            'topic4_icon' => 'library_images/library_icon_attributes.png',
            'topic4_link' => '#',

            // Topic 5
            'topic5_label' => 'Bitwise Operators',
            'topic5_icon' => 'library_images/library_icon_bitwise.png',
            'topic5_link' => '#',

            // Topic 6
            'topic6_label' => 'Boolean Logic',
            'topic6_icon' => 'library_images/library_icon_boolean.png',
            'topic6_link' => '#',

            // Topic 7
            'topic7_label' => 'Classes',
            'topic7_icon' => 'library_images/library_icon_classes.png',
            'topic7_link' => '#',

            // Topic 8
            'topic8_label' => 'Comprehensions',
            'topic8_icon' => 'library_images/library_icon_comprehension.png',
            'topic8_link' => '#',

            // Topic 9
            'topic9_label' => 'Concurrency',
            'topic9_icon' => 'library_images/library_icon_concurrency.png',
            'topic9_link' => '#',

            // Topic 10
            'topic10_label' => 'Context Managers',
            'topic10_icon' => 'library_images/library_icon_context.png',
            'topic10_link' => '#',
        ];

        return view('library', compact('LibraryPage'));
    }
}
