const apiUrl = 'http://localhost:3000/blog/api/post-list/';
const postsSection = document.getElementById('posts');

async function fetchAndDisplayPosts() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();

    for (const post of data.results) {
      const articleElement = document.createElement('article');
      articleElement.classList.add('post-item');

      const thumbnailElement = document.createElement('img')
      if (post.thumbnail) {
        thumbnailElement.src = post.thumbnail
        thumbnailElement.width = 200
        thumbnailElement.height = 200
        articleElement.appendChild(thumbnailElement)
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
          console.warn(`Could not fetch author data for ID: ${authorId}`);
          const authorElement = document.createElement('p');
          authorElement.textContent = 'نویسنده: نامشخص';
          articleElement.appendChild(authorElement);
        } else {
          const authorData = await authorResponse.json();
          const authorName = authorData.get_full_name

          const authorElement = document.createElement('p');
          authorElement.textContent = `نویسنده: ${authorName}`;
          articleElement.appendChild(authorElement);
        }
      } catch (authorError) {
        console.error(`Error fetching author data for post ${post.id}:`, authorError);
        const authorElement = document.createElement('p');
        authorElement.textContent = 'نویسنده: خطا در بارگیری';
        articleElement.appendChild(authorElement);
      }

      postsSection.appendChild(articleElement);
    }
  } catch (error) {
    console.error('Error fetching posts:', error);
    postsSection.innerHTML = '<p>خطا در بارگیری پست‌ها. لطفاً بعداً دوباره تلاش کنید.</p>';
  }
}

fetchAndDisplayPosts();
