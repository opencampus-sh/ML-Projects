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
          title: 'Docs',
          items: [
            {
              label: 'Style Guide',
              to: 'docs/',
            },
            {
              label: 'Second Doc',
              to: 'docs/doc2/',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
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
            'https://github.com/facebook/docusaurus/edit/master/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
