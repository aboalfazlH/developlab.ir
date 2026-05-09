const apiUrlBase = `http://${window.location.host}/blog/api/post-list/`;
const postsSection = document.getElementById('posts');
const paginationContainer = document.getElementById('pagination');

function createTextItem(post) {
    const container = document.createElement('article');
    const child = document.createElement('div');
    container.classList.add('post-item');
    container.style.cursor = 'pointer';

    if (post.thumbnail) {
        const img = document.createElement('img');
        img.src = post.thumbnail;
        img.width = 200;
        img.height = 200;
        img.alt = post.title;
        container.appendChild(img);
    }


    const title = document.createElement('h4');
    title.textContent = post.title;
    child.appendChild(title);

    const date = document.createElement('p');
    date.innerHTML = `تاریخ انتشار: ${new Date(post.write_date).toLocaleDateString('fa-IR')}`;
    child.appendChild(date);

    (async () => {
        try {
            const authorResponse = await fetch(`http://${window.location.host}/accounts/api/users/${post.author}`);
            if (!authorResponse.ok) throw new Error('Author fetch failed');
            const authorData = await authorResponse.json();
            const authorName = authorData.__str__ || 'نامشخص';

            const authorEl = document.createElement('p');
            authorEl.textContent = `نویسنده: ${authorName}`;
            child.insertBefore(authorEl, child.lastElementChild);
        } catch (error) {
            console.error(`Error fetching author for post ${post.id}:`, error);
            const authorEl = document.createElement('p');
            authorEl.textContent = 'نویسنده: نامشخص';
            child.insertBefore(authorEl, child.lastElementChild);
        }
    })();

    const seeBtn = document.createElement('a');
    seeBtn.href = `http://${window.location.host}/${post.get_absolute_url}`;
    seeBtn.textContent = "مشاهده پست";
    seeBtn.classList.add("see")
    child.appendChild(seeBtn);
    container.appendChild(child);

    return container;
}

async function fetchAndDisplayPosts(page = 1) {
    postsSection.innerHTML = '';
    if (paginationContainer) paginationContainer.innerHTML = '';

    try {
        const response = await fetch(`${apiUrlBase}?page=${page}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            postsSection.innerHTML = '<h2 class="not-found">پستی یافت نشد.</h2>';
            if (paginationContainer) paginationContainer.innerHTML = '';
            return;
        }

        for (const post of data.results) {
            const postElement = createTextItem(post);

            postElement.addEventListener('click', (e) => {
                if (e.target.tagName !== 'A') {
                    if (window.protocol) {
                        window.location = `${window.protocol}//${window.location.host}/${post.get_absolute_url}`;
                    } else {
                        window.location = `http://${window.location.host}/${post.get_absolute_url}`;
                    }
                }
            });

            postsSection.appendChild(postElement);
        }

        createPaginationControls(data, page);

    } catch (error) {
        console.error('Error fetching posts:', error);
        postsSection.innerHTML = '<p class="error">خطایی در بارگذاری پست‌ها رخ داد.</p>';
    }
}

function createPaginationControls(data, currentPage) {
    if (!paginationContainer) return;

    const totalPages = data.num_pages || 1;

    if (totalPages <= 1) return;

    const ul = document.createElement('ul');
    ul.style.display = 'flex';
    ul.style.listStyle = 'none';
    ul.style.padding = '10px';
    ul.style.gap = '5px';
    ul.style.justifyContent = 'center';

    const prevLi = document.createElement('li');
    const prevBtn = document.createElement('button');
    prevBtn.textContent = 'قبلی';
    prevBtn.disabled = !data.previous;

    prevBtn.onclick = () => {
        if (currentPage > 1) {
            fetchAndDisplayPosts(currentPage - 1);
        }
    };
    prevLi.appendChild(prevBtn);
    ul.appendChild(prevLi);

    for (let i = 1; i <= totalPages; i++) {
        const li = document.createElement('li');
        const btn = document.createElement('button');
        btn.textContent = i;

        if (i === currentPage) {
            btn.style.fontWeight = 'bold';
            btn.style.backgroundColor = '#ddd';
        }

        btn.onclick = () => {
            if (i !== currentPage) {
                fetchAndDisplayPosts(i);
            }
        };

        li.appendChild(btn);
        ul.appendChild(li);
    }

    const nextLi = document.createElement('li');
    const nextBtn = document.createElement('button');
    nextBtn.textContent = 'بعدی';
    nextBtn.disabled = !data.next;

    nextBtn.onclick = () => {
        if (currentPage < totalPages) {
            fetchAndDisplayPosts(currentPage + 1);
        }
    };
    nextLi.appendChild(nextBtn);
    ul.appendChild(nextLi);

    paginationContainer.appendChild(ul);
}

fetchAndDisplayPosts(1);