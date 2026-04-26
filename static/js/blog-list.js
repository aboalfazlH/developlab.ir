const apiUrl = 'http://localhost:3000/blog/api/post-list/';
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const postsSection = document.getElementById('posts');
    data.results.forEach(post => {
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
      } else if (post.description) {
        if (post.description.length >= 140) {
          const part1 = post.description.slice(0, 100);
          const part2 = post.description.slice(100, 200);
          const part3 = post.description.slice(200, 300);
          
          if (post.description.length > 140 && post.description.length <= 280) {
            descriptionElement.innerHTML = part1 + "<br>" + part2;
          } else if (post.description.length > 280) {
            descriptionElement.innerHTML = part1 + "<br>" + part2 + "<br>" + part3 + "...";
          } else {
            descriptionElement.textContent = post.description;
          }
        } else {
          descriptionElement.textContent = post.description;
        }
      } else {
        descriptionElement.textContent = post.description;
      }
      
      articleElement.appendChild(descriptionElement);
      
      

      const dateElement = document.createElement('p');
      dateElement.innerHTML = `تاریخ انتشار: ${new Date(post.write_date).toLocaleDateString('fa-IR')}`;
      articleElement.appendChild(dateElement);
      
      postsSection.appendChild(articleElement);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });