import { notFound } from 'next/navigation';
import { navConfig } from '@/config/nav';
import { Sidebar } from '@/components/layout/sidebar';

function unslugify(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

export default function SectionLayout({ children, params }) {
  const { section } = params;
  const sidebarNav = navConfig.sidebarNav[section];

  if (!sidebarNav) {
    notFound();
  }

  return (
    <div className="h-full grid grid-cols-1 md:grid-cols-[auto_1fr]">
      <Sidebar items={sidebarNav} sectionTitle={unslugify(section)} />
      <main className="flex-1 p-6 sm:p-8 lg:p-10 overflow-y-auto">
        {children}
      </main>
    </div>
  );
}
