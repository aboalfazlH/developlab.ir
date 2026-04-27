const apiUrlBase = 'http://localhost:3000/blog/api/post-list/';
const postsSection = document.getElementById('posts');
const paginationContainer = document.getElementById('pagination');

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
      return;
    }

    for (const post of data.results) {
      const articleElement = document.createElement('article');
      articleElement.classList.add('post-item');
      
      const thumbnailElement = document.createElement('img');
      if (post.thumbnail) {
        thumbnailElement.src = post.thumbnail;
        thumbnailElement.width = 200;
        thumbnailElement.height = 200;
        thumbnailElement.alt = post.title;
        articleElement.appendChild(thumbnailElement);
      }

      const titleElement = document.createElement('h3');
      titleElement.textContent = post.title;
      articleElement.appendChild(titleElement);

      const descriptionElement = document.createElement('p');
      if (post.summary) {
        descriptionElement.textContent = post.summary;
        articleElement.appendChild(descriptionElement);
      }

      const dateElement = document.createElement('p');
      dateElement.innerHTML = `تاریخ انتشار: ${new Date(post.write_date).toLocaleDateString('fa-IR')}`;
      articleElement.appendChild(dateElement);

      try {
        const authorId = post.author;
        const authorResponse = await fetch(`http://localhost:3000/accounts/api/users/${authorId}`);
        if (!authorResponse.ok) {
          throw new Error('Author fetch failed');
        }
        const authorData = await authorResponse.json();
        const authorName = authorData.__str__;
        const authorElement = document.createElement('p');
        authorElement.textContent = `نویسنده: ${authorName}`;
        articleElement.appendChild(authorElement);
      } catch (authorError) {
        console.error(`Error fetching author data for post ${post.id}:`, authorError);
        const authorElement = document.createElement('p');
        authorElement.textContent = 'نویسنده: نامشخص';
        articleElement.appendChild(authorElement);
      }

      postsSection.appendChild(articleElement);
    }

    createPaginationControls(data, page);

  } catch (error) {
    console.error('Error fetching posts:', error);
    postsSection.innerHTML = '<p>خطا در بارگیری پست‌ها. لطفاً بعداً دوباره تلاش کنید.</p>';
  }
}

function createPaginationControls(data, currentPage) {
  if (!paginationContainer) return;

  const totalPages = data.num_pages;
  const count = data.count;
  
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
    if (data.previous) {
      const urlParams = new URLSearchParams(new URL(data.previous).search);
      
      const prevPage = parseInt(urlParams.get('page'));
      if (isNaN(prevPage)) {
        fetchAndDisplayPosts(1)
      }
      fetchAndDisplayPosts(prevPage);
    }
  };
  prevLi.appendChild(prevBtn);
  ul.appendChild(prevLi);
  
  for (let i = 1; i <= totalPages; i++) {
    const li = document.createElement('li');
    const btn = document.createElement('button');
    btn.textContent = i;
    
    btn.onclick = () => fetchAndDisplayPosts(i);
    li.appendChild(btn);
    ul.appendChild(li);
  }
  
  const nextLi = document.createElement('li');
  const nextBtn = document.createElement('button');
  nextBtn.textContent = 'بعدی';
  nextBtn.disabled = !data.next;
  nextBtn.onclick = () => {
    if (data.next) {
      const urlParams = new URLSearchParams(new URL(data.next).search);
      const nextPage = parseInt(urlParams.get('page'));
      fetchAndDisplayPosts(nextPage);
    }
  };
  nextLi.appendChild(nextBtn);
  ul.appendChild(nextLi);

  paginationContainer.appendChild(ul);
}

fetchAndDisplayPosts(1);