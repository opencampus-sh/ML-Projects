module.exports = {
  title: 'Opencampus.sh Machine Learning Projects',
  tagline: 'This site offers an overview about all the projects done within the Opencampus Machine Learning Degree. Check below the projects for each course or go to the Machine Learning Degree Website.',
  url: 'https://opencampus-sh.github.io',
  baseUrl: '/ML-Projects/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/logo_OC.ico',
  organizationName: 'opencampus-sh', // Usually your GitHub org/user name.
  projectName: 'ml-projects', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'OC ML Degree',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo_OC.png',
      },
      items: [
        {
          to: 'dl',
          label: 'Deep Learning',
          position: 'left',
        },
        {to: 'mlt', label: 'Tensorflow', position: 'left'},
        {to: 'nlp', label: 'Natural Language Processing', position: 'left'},
        {
          href: 'https://github.com/opencampus-sh/ML-Projects',
          label: 'GitHub Repo',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Courses',
          items: [
            {
              label: 'Deep Learning',
              to: 'dl',
            },
            {
              label: 'Machine Learning with Tensorflow',
              to: 'mlt',
            },
            {
              label: 'Natural Language Processing',
              to: 'nlp',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Mattermost',
              href: 'https://chat.opencampus.sh',
            },
            {
              label: 'Slack',
              href: 'https://opencampus-sh.slack.com',
            },
            {
              label: 'KielAI',
              href: 'https://kiel.ai/',
            },
          ],
        },
        {
          title: 'Opencampus',
          items: [
            {
              label: 'opencampus.sh',
              to: 'https://opencampus.sh',
            },
            {
              label: 'EDU Hub',
              href: 'https://edu.opencampus.sh',
            },
            {
              label: 'Machine Learning Degree',
              href: 'https://edu.opencampus.sh/courses/158',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Opencampus. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/opencampus-sh/ML-Projects/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/opencampus-sh/ML-Projects/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
