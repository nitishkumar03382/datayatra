// add tailwind modern UI to markdown html 
// Apply tailwind css to description tables and make table scrollable inside description div
document.querySelectorAll('.description').forEach(description => {
    description.classList.add('bg-white', 'p-4', 'rounded-lg', 'shadow-md', 'my-4');
    // Add a scrollbar for long content
    description.style.overflowY = 'auto';
    description.style.maxHeight = '600px'; // Set a max height for the description div
});
document.querySelectorAll('.description table').forEach(table => {
    table.classList.add('min-w-full', 'border-collapse', 'border', 'border-gray-300', 'rounded-lg', 'shadow-md', 'my-4');
    table.querySelectorAll('th').forEach(th => {
        th.classList.add('px-4', 'py-2', 'bg-gray-200', 'text-left', 'font-semibold');
    });
    table.querySelectorAll('td').forEach(td => {
        td.classList.add('px-4', 'py-1', 'border-t', 'border-gray-300');
    });
});
// Apply tailwind css to description lists
document.querySelectorAll('.description dl').forEach(dl => {
    dl.classList.add('grid', 'grid-cols-1', 'sm:grid-cols-2', 'gap-4', 'my-4');
    dl.querySelectorAll('dt').forEach(dt => {
        dt.classList.add('font-semibold', 'text-gray-700');
    });
    dl.querySelectorAll('dd').forEach(dd => {
        dd.classList.add('text-gray-600');
    });
});
// Apply tailwind css to description paragraphs
document.querySelectorAll('.description p').forEach(p => {
    p.classList.add('text-gray-700', 'my-2');
});
// Apply tailwind css to description headings
document.querySelectorAll('.description h1, .description h2, .description h3').forEach(heading => {
    heading.classList.add('text-gray-800', 'font-bold', 'my-4');
    if (heading.tagName === 'H1') {
        heading.classList.add('text-2xl');
    } else if (heading.tagName === 'H2') {
        heading.classList.add('text-xl');
    } else if (heading.tagName === 'H3') {
        heading.classList.add('text-lg');
    }
});
// Apply tailwind css to description code blocks
document.querySelectorAll('.description').forEach(pre => {
    pre.querySelectorAll('code').forEach(code => {
        code.classList.add('text-sm', 'text-green-800', 'font-mono',  'rounded-sm', 'shadow-sm');
        code.style.whiteSpace = 'pre-wrap'; // Ensure code wraps properly
        // remove ` from the start and end of the code block
        
        
    });
});
// Apply tailwind css to description lists
document.querySelectorAll('.description ul, .description ol').forEach(list => {
    list.classList.add('list-disc', 'pl-5', 'my-2');
    list.querySelectorAll('li').forEach(li => {
        li.classList.add('text-gray-700', 'my-1');
    });
});

// Apply tailwind css to scrollable divs
document.querySelectorAll('.scrollable').forEach(scrollable => {
    scrollable.classList.add('overflow-y-auto', 'max-h-96', 'p-4', 'bg-white', 'rounded-sm', 'shadow-md');
});