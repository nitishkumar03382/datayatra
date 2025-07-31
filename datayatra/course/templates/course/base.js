// === Dark Mode Styling for .description Sections (LeetCode Style) ===

// Style the main description container
document.querySelectorAll('.description').forEach(description => {
    description.classList.add(
        'bg-stone-900', 'text-stone-100', 'p-5', 'rounded-lg', 'shadow-lg', 'my-6', 'overflow-y-auto'
    );
    description.style.maxHeight = '600px';
});

// Style <table> inside .description
document.querySelectorAll('.description table').forEach(table => {
    table.classList.add(
        'min-w-full', 'border-collapse', 'rounded-lg', 'overflow-hidden', 'my-4'
    );
    table.querySelectorAll('th').forEach(th => {
        th.classList.add(
            'px-4', 'py-2', 'bg-stone-800', 'text-stone-200', 'text-sm', 'text-left', 'border-b', 'border-stone-700'
        );
    });
    table.querySelectorAll('td').forEach(td => {
        td.classList.add(
            'px-4', 'py-2', 'border-b', 'border-stone-700', 'text-stone-300', 'text-sm'
        );
    });
});

// Style <dl> definition lists
document.querySelectorAll('.description dl').forEach(dl => {
    dl.classList.add('grid', 'grid-cols-1', 'sm:grid-cols-2', 'gap-4', 'my-4');
    dl.querySelectorAll('dt').forEach(dt => {
        dt.classList.add('font-semibold', 'text-stone-300');
    });
    dl.querySelectorAll('dd').forEach(dd => {
        dd.classList.add('text-stone-400');
    });
});

// Style <p> paragraphs
document.querySelectorAll('.description p').forEach(p => {
    p.classList.add('text-stone-300', 'my-3', 'leading-relaxed');
});

// Style headings
document.querySelectorAll('.description h1, .description h2, .description h3').forEach(heading => {
    heading.classList.add('font-bold', 'my-4', 'text-stone-100');
    if (heading.tagName === 'H1') {
        heading.classList.add('text-2xl');
    } else if (heading.tagName === 'H2') {
        heading.classList.add('text-xl');
    } else if (heading.tagName === 'H3') {
        heading.classList.add('text-lg');
    }
});

// Style inline <code> elements
document.querySelectorAll('.description code').forEach(code => {
    const isBlock = code.parentElement.tagName === 'PRE';
    code.classList.add('font-mono', 'rounded', 'whitespace-pre-wrap');

    if (isBlock) {
        code.classList.add(
            'bg-stone-800', 'text-green-400', 'p-4', 'block', 'overflow-x-auto', 'text-sm'
        );
    } else {
        code.classList.add(
            'bg-stone-800', 'text-green-300', 'px-1.5', 'py-0.5', 'text-sm'
        );
    }
});

// Style <pre> blocks directly
document.querySelectorAll('.description pre').forEach(pre => {
    pre.classList.add(
        'bg-stone-800', 'rounded-lg', 'p-4', 'my-4', 'overflow-x-auto', 'text-sm'
    );
});

// Style unordered and ordered lists
document.querySelectorAll('.description ul, .description ol').forEach(list => {
    list.classList.add('pl-6', 'my-4');
    list.querySelectorAll('li').forEach(li => {
        li.classList.add('text-stone-300', 'mb-2', 'list-disc');
    });
});

// Optional: Style scrollable divs
document.querySelectorAll('.scrollable').forEach(scrollable => {
    scrollable.classList.add(
        'overflow-y-auto', 'max-h-96', 'p-4', 'bg-stone-800', 'rounded-md', 'shadow-md'
    );
});

// Optional: Style list-chapters panel
document.querySelectorAll('.list-chapters').forEach(chapterList => {
    chapterList.classList.add(
        'overflow-y-auto', 'max-h-96', 'p-4', 'bg-stone-800', 'rounded-lg', 'shadow-md'
    );
});
