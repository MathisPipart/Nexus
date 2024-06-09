function toggleText(button) {
    const postTextContainer = button.closest('.post_text'); // Trouve le conteneur du post parent
    const postTruncateText = postTextContainer.querySelector('.post-truncate-text');
    const postFullText = postTextContainer.querySelector('.post-full-text');

    if (postTruncateText.style.display === 'none') {
        postTruncateText.style.display = 'block';
        postFullText.style.display = 'none';
    } else {
        postTruncateText.style.display = 'none';
        postFullText.style.display = 'block';
    }
}